const express = require("express")
const path = require("path")

const app = express()
const PYTHON_API_URL = process.env.PYTHON_API_URL || "http://127.0.0.1:8000"   // FastAPI (radio /stations)
const ISS_API_URL = process.env.ISS_API_URL || "http://127.0.0.1:5000"
const HARDCODED_FALLBACK_COUNTRY = "Nigeria"  

app.use(express.static(path.join(__dirname, "public")))
app.set("views", path.join(__dirname, "views"))
app.set("view engine", "ejs")
app.engine("ejs", require("ejs").__express)

async function getIssCountry() {
  try {
    const issRes = await fetch(ISS_API_URL, { signal: AbortSignal.timeout(4000) })
    const [latitude, longitude] = await issRes.json()
    const geoRes = await fetch(
      `https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=jsonv2`,
      { headers: { "User-Agent": "whatISSgoingon/1.0" }, signal: AbortSignal.timeout(4000) }
    )
    const geo = await geoRes.json()
    const country = geo.address && geo.address.country
    if (country) return { country, source: "iss_tracker" }
  } catch (err) {
  }
  return { country: HARDCODED_FALLBACK_COUNTRY, source: "HARDCODED_FALLBACK" }   // !!! HARDCODED !!!
}

app.get("/", async (req, res) => {
  const { country } = await getIssCountry()
  res.render("index", { country })
})

app.get("/api/iss-country", async (req, res) => {
  res.json(await getIssCountry())
})

app.get("/api/stations", async (req, res) => {
  try {
    const pythonResponse = await fetch(`${PYTHON_API_URL}/stations?country=${encodeURIComponent(req.query.country || "")}`)
    const data = await pythonResponse.json()
    res.status(pythonResponse.status).json(data)
  } catch (err) {
    res.status(502).json({ error: "Python backend unreachable" })
  }
})
 
app.get("/api/weather", async (req,res) => {
    const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${req.query.latitude}&longitude=${req.query.longitude}&current=temperature_2m`)
    const data =  await response.json()
    res.status(response.status).json(data)

if (require.main === module) app.listen(3000)
module.exports = app
