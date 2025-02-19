import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AnalyticsService {

  private baseUrl = 'http://127.0.0.1:8000'; // Update if needed

  constructor(private http: HttpClient) { }

  // Get transactions from the last X days
  getTransactions(days: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/transactions/${days}`);
  }

  // Get real-time fraud alerts
  getFraudAlerts(): Observable<any> {
    return this.http.get(`${this.baseUrl}/fraud-alerts/realtime`);
  }
}
