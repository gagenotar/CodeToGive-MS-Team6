import React from "react"
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />}/>
        <Route path="/logout" element={<Logout />}/>
        <Route path="/register" element={<RegisterAndLogout />}/>
        <Route path="/home" element={<Home />}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App