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


app.listen(3000)