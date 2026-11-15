const myImageUrl =
  'https://cdn.jsdelivr.net/npm/three-globe/example/img/earth-blue-marble.jpg'

const myData = [
  { lat: 6.4654, lng: 3.3970, name: 'Test marker near McMaster' }
]

const response = await fetch("/countries.geojson")
const countries = await response.json()


const myGlobe = new Globe(document.getElementById('globe'),{animatein:true})
  .globeImageUrl(myImageUrl)
  .showAtmosphere(true)
  .atmosphereColor('dodgerblue')
  .atmosphereAltitude(0.3);



const nigeria = countries.features.find(
  country => country.properties.name === 'Ghana'
)

myGlobe.polygonsData(nigeria ? [nigeria] : [])