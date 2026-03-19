package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"html/template"
	"net/http"
	"os"
)

type Transaction struct {
	User     string  `json:"user"`
	Amount   float64 `json:"amount"`
	Currency string  `json:"currency"`
}

func main() {
	backendURL := os.Getenv("BACKEND_URL")
	if backendURL == "" {
		backendURL = "http://localhost:8000"
	}

	tmpl := template.Must(template.ParseFiles("templates/index.html"))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == http.MethodPost {
			amount := 0.0
			fmt.Sscanf(r.FormValue("amount"), "%f", &amount)

			tx := Transaction{
				User:     r.FormValue("user"),
				Amount:   amount,
				Currency: r.FormValue("currency"),
			}

			jsonData, _ := json.Marshal(tx)
			resp, err := http.Post(backendURL+"/transactions", "application/json", bytes.NewBuffer(jsonData))

			status := "Success!"
			if err != nil || resp.StatusCode != 200 {
				status = "Error sending transaction!"
			}
			
			tmpl.Execute(w, map[string]interface{}{"Status": status})
			return
		}
		tmpl.Execute(w, nil)
	})

	fmt.Println("Go Frontend is running on port 8080...")
	http.ListenAndServe(":8080", nil)
}