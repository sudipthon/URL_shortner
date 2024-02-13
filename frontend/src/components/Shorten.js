import { useState } from "react";
import React from 'react';
function Shorten() {
  let host = window.location.origin;
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");

  const shortenUrl = () => {
    // fetch("http://127.0.0.1:8000/", {
    fetch("https://bug12.pythonanywhere.com/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        original_url: url,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        setShortUrl(`${host}/${data.short_url}`);
        navigator.clipboard.writeText(`${host}/${data.short_url}`);
        setUrl("");
        // setShortUrl("");
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="rounded px-2 py-1 mx-2 border-2 border-blue-400"
      />
      <button onClick={shortenUrl}
       className="
       rounded px-2 py-1 text-white bg-blue-400 text-center
       "
      >Shorten</button>
      {shortUrl && <p className="text-white my-1 mx-2" >Short URL : {shortUrl}</p>}
    </div>
  );
}

export default Shorten;
