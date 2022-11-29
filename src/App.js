import React from 'react'
import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'
import PageNotFound from './pages/PageNotFound'

const App = ()=> {
	return (
		<BrowserRouter>
			<Routes>
				<Route exact path='/index.html' component={Home} />
				<Route path='/about.html' component={About} />
				<Route path='/404.html' component={PageNotFound} />
			</Routes>
		</BrowserRouter>
	)
}
export default App
