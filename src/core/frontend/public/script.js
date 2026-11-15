const myImageUrl =
  'https://cdn.jsdelivr.net/npm/three-globe/example/img/earth-blue-marble.jpg'

// const myData = [
//   { lat: 6.4654, lng: 3.3970, name: 'Test marker near McMaster' }
// ]

//Country Highlighting
const response = await fetch("/countries.geojson")
const countries = await response.json()

// ISS location
const issResponse = await fetch('https://api.wheretheiss.at/v1/satellites/25544')
const iss = await issResponse.json()


// Weather code
const weatherResponse = await fetch(
  `/api/weather?latitude=${iss.latitude}&longitude=${iss.longitude}`
)
const weatherData = await weatherResponse.json()

if (weatherResponse.ok) {
  document.getElementById('temperature').textContent =
    `Temperature below the ISS: ${weatherData.current.temperature_2m}°C`
}

async function updateImages() {
  const container = document.getElementById('location-images')
  const status = document.getElementById('images-status')
  container.replaceChildren()

  try {
    const response = await fetch(
      `/api/images?latitude=${iss.latitude}&longitude=${iss.longitude}&limit=3`
    )

    if (!response.ok) throw new Error('Image request failed')

    const photos = await response.json()

    for (const photo of photos) {
      const imageUrl = photo.thumb_url || photo.full_url
      if (!imageUrl) continue

      const image = document.createElement('img')
      image.src = imageUrl
      image.alt = photo.title || 'Nearby location'
      image.width = 250
      image.loading = 'lazy'

      container.appendChild(image)
    }

    status.textContent = container.children.length
      ? ''
      : 'No nearby photos available.'
  } catch (error) {
    status.textContent = 'Photos unavailable right now.'
    console.error(error)
  }
}

updateImages()
//Reverse Geocoding
const url = `https://nominatim.openstreetmap.org/reverse?lat=${iss.latitude}&lon=${iss.longitude}&format=jsonv2`
const locationResponse = await fetch(url)
const locationData = await locationResponse.json()
const country = locationData.address?.country
const countryCode = locationData.address?.country_code?.toUpperCase()


let lastTunedCountry = null

async function updateRadio() {
  const code = countryCode ?? lastTunedCountry ?? 'NG'
  if (!code || code === lastTunedCountry) return

  const response = await fetch(`/api/stations?country=${encodeURIComponent(code)}`)
  if (!response.ok) return

  const data = await response.json()

  const streamUrl = data.stations?.find(station =>
  station.url_resolved &&
  !station.url_resolved.toLowerCase().includes('.m3u8')
)?.url_resolved

  const player = document.getElementById('radio-player')
  const wasPlaying = !player.paused

  player.src = streamUrl
  lastTunedCountry = code

  if (wasPlaying) {
    player.play().catch(error => console.warn('Could not play the new station', error))
  }
}










//Radio 
const MIRROR_SERVERS = [
    "https://de1.api.radio-browser.info",
    "https://nl1.api.radio-browser.info",
    "https://at1.api.radio-browser.info",
]





const myGlobe = new Globe(document.getElementById('globe'),{animatein:true})
  .globeImageUrl(myImageUrl)
  .showAtmosphere(true)
  .atmosphereColor('dodgerblue')
  .atmosphereAltitude(0.3);




function findCountryPolygon(name) {
    const country_ = countries.features.find(country => country.properties.name === name)
    return country_
}


document.getElementById("country-name").textContent = country ? `Currently above ${country}` : 'No country Below'

const country_polygon = countryCode
  ? countries.features.find(
      feature => feature.properties['ISO3166-1-Alpha-2'] === countryCode
    )
  : undefined

myGlobe.polygonsData(country_polygon ? [country_polygon] : [])
updateRadio()
setInterval(updateRadio, 90_000)