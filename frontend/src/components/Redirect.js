import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { useState } from 'react';
import React from 'react';

export default function Redirect() {
  const { redirect } = useParams();
  const [urlFound, setUrlFound] = useState(true);

  useEffect(() => {
    const fetchUrl = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:8000/short/${redirect}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        if (!response.ok) {
          // throw new Error(`HTTP error! status: ${response.status}`);
          setUrlFound(false);

        }
        const data = await response.json();
        if (data.original_url) {
          window.location.href = data.original_url;
        }
      } catch (error) {
        console.error("Fetch error:", error);
      }
    };

    fetchUrl();
  }, [redirect]);
  return (
    !urlFound && <p className="text-white">No URL found for the given short URL.</p>
  );
}
