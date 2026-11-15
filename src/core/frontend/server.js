const express = require("express")

const app = express()

app.use(express.static('public'));
app.set("view engine", "ejs")

app.get("/",(req,res) => {
    res.render("index",{country: "Nigeria"})
    // res.sendFile()
})

app.get('/api/stations', async (req, res) => {
  const pythonResponse = await fetch(`http://127.0.0.1:8000/stations?country=${req.query.country}`)
  const data = await pythonResponse.json()
  res.status(pythonResponse.status).json(data)
})

app.get('/api/images', async (req, res) => {
  const imageApiUrl = new URL('http://127.0.0.1:8000/images')
  for (const parameter of ['latitude', 'longitude', 'radius', 'limit']) {
    if (req.query[parameter] !== undefined) {
      imageApiUrl.searchParams.set(parameter, String(req.query[parameter]))
    }
  }

  try {
    const pythonResponse = await fetch(imageApiUrl)
    const data = await pythonResponse.json()
    res.status(pythonResponse.status).json(data)
  } catch (error) {
    console.error('Failed to fetch images from the Python API:', error)
    res.status(502).json({ error: 'Image service is unavailable' })
  }
})
 
app.get("/api/weather", async (req,res) => {
    const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${req.query.latitude}&longitude=${req.query.longitude}&current=temperature_2m`)
    const data =  await response.json()
    res.status(response.status).json(data)


})

app.listen(3000)