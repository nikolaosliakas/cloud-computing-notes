// 1. Import the libraries
const express = require('express')
const app = express()

const movieRoute = require('./routes/movies')
const userRoute = require('./routes/users')

// 2. Middleware
app.use('/movies', movieRoute) // when user navigates from / to /movies go to movieRoute
app.use('/users', userRoute)

// 3. Create a route
app.get('/', (req, res)=> {
    res.send('You are in your home page!')
})


// 4. Start the server 
app.listen(3000, ()=>{
    console.log('Server is up and running')
})