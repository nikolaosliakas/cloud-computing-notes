const express = require('express')
const app = express()

const mongoose = require('mongoose')
const bodyParser = require('body-parser')
require('dotenv/config')

const filmsRoute = require('./routes/films')
app.use('/api/film', filmsRoute)

mongoose.connect(process.env.DB_CONNECTOR).then(()=>{
    console.log('DB is connected')
})

app.listen(3000, ()=>{
    console.log('Server is running')
})