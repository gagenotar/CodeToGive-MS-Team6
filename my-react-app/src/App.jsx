import React from "react"
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import Profile from "./pages/Profile"
import LoginAdmin from "./pages/AdminLogin"
import RegisterAdmin from "./pages/AdminRegister"
import Admin from "./pages/Admin"

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function RegisterAndLogoutAdmin() {
  localStorage.clear()
  return <RegisterAdmin />
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />}/>
        <Route path="/register" element={<RegisterAndLogout />}/>
        <Route path="/logout" element={<Logout />}/>
        <Route path="/home" element={<Home />}/>
        <Route path="/login/admin" element={<LoginAdmin />}/>
        <Route path="/register/admin" element={<RegisterAndLogoutAdmin />}/>
        <Route path="/admin" element={<Admin />}/>
        <Route path="/profile" element={<Profile />}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App