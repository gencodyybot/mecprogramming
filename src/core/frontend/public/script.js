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

//Reverse Geocoding
const url = `https://nominatim.openstreetmap.org/reverse?lat=${iss.latitude}&lon=${iss.longitude}&format=jsonv2`
const locationResponse = await fetch(url)
const locationData = await locationResponse.json()
const country = locationData.address?.country



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

const country_polygon = findCountryPolygon(country)
console.log({
  status: locationResponse.status,
  locationData,
  country,
  matched: Boolean(country_polygon)
})

myGlobe.polygonsData(country_polygon ? [country_polygon] : [])