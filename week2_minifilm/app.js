const express = require('express')
const app = express()

const mongoose = require('mongoose')

const filmsRoute = require('./routes/films')

app.use('/films', filmsRoute)

app.get('/', (req, res)=>{
    res.send('Homepage')
})

const MURL = 'mongodb+srv://student:1234@cluster.qz1mk.mongodb.net/MiniFilms?retryWrites=true&w=majority'
mongoose.set('strictQuery', true)
mongoose.connect(MURL, ()=>{
    console.log('Your mongoDB connector is on')
})

app.listen(3000, ()=>{
    console.log('Your server is up and running!')
})