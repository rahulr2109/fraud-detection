// src/app/services/fraud-alerts.service.ts
import { Injectable } from '@angular/core';
import { Observable, Observer } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FraudAlertsService {
  private ws: WebSocket;

  constructor() {
    this.ws = new WebSocket("ws://localhost:8000/ws/fraud");
  }

  /**
   * Returns an Observable that emits fraud alert messages received from the WebSocket.
   */
  public getFraudAlerts(): Observable<any> {
    return new Observable((observer: Observer<any>) => {
      this.ws.onopen = () => {
        console.log("WebSocket connection established.");
      };

      this.ws.onmessage = (event) => {
        console.log("WebSocket message received:", event.data);
        try {
          const data = JSON.parse(event.data);
          observer.next(data);
        } catch (error) {
          observer.error(error);
        }
      };

      this.ws.onerror = (error) => {
        console.error("WebSocket error:", error);
        observer.error(error);
      };

      this.ws.onclose = () => {
        console.log("WebSocket connection closed.");
        observer.complete();
      };

      // Cleanup logic when the subscription is closed
      return () => {
        this.ws.close();
      };
    });
  }
}
