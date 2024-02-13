import "./App.css";
import React from 'react';
import Shorten from "./components/Shorten";
import Redirect from "./components/Redirect";

import { BrowserRouter, Route, Routes } from "react-router-dom";

export default function App() {
  return (
    <div className="h-screen mx-auto flex flex-col items-center bg-gray-600 justify-center">

    <BrowserRouter>
      <Routes>
          <Route path='/' element={<Shorten/>}/>
          <Route path='/:redirect' element={<Redirect/>}/>
      </Routes>
    </BrowserRouter>
    </div>
  );
}
