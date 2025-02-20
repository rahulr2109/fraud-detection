import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FraudAlertsService } from '../../services/fraud-alerts.service';

@Component({
  selector: 'app-fraud-alerts',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './fraud-alerts.component.html',
  styleUrls: ['./fraud-alerts.component.scss']
})
export class FraudAlertsComponent implements OnInit {
  alerts: any[] = [];

  constructor(private fraudAlertsService: FraudAlertsService) {}

  ngOnInit(): void {
    this.fraudAlertsService.getFraudAlerts().subscribe({
      next: (data) => {
        console.log("Received fraud alert:", data);
        // Append each new alert to the alerts array
        this.alerts.push(data);
      },
      error: (err) => console.error("WebSocket error:", err)
    });
  }
}
