package main

import (
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		log.Printf("accessed from %s", r.RemoteAddr)
		w.Write([]byte("OK\n\r"))
	})
	http.ListenAndServe("0.0.0.0:8080", nil)
}
