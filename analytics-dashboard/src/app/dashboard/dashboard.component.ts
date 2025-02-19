import { Component, OnInit, AfterViewInit, ViewChild, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AnalyticsService } from '../services/analytics.service';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    MatTableModule,
    MatPaginatorModule,
    MatSortModule
  ],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit, AfterViewInit {
  // Data arrays
  transactions: any[] = [];
  fraudAlerts: any[] = [];
  days: number = 7; // Last 7 days

  // Error messages for each API call
  transactionsErrorMessage: string = '';
  fraudAlertsErrorMessage: string = '';

  // Table configuration for transactions
  displayedColumns: string[] = ['transaction_id', 'amount', 'timestamp'];
  dataSource = new MatTableDataSource<any>(this.transactions);
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  // Table configuration for fraud alerts
  displayedColumnsFraud: string[] = ['transaction_id', 'amount', 'timestamp'];
  fraudAlertsDataSource = new MatTableDataSource<any>(this.fraudAlerts);
  @ViewChild('fraudAlertsPaginator') fraudAlertsPaginator!: MatPaginator;

  constructor(private analyticsService: AnalyticsService, private cdRef: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.loadTransactions();
    this.loadFraudAlerts();
  }

  ngAfterViewInit(): void {
    // Assign paginator and sort for transactions table
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
    this.paginator.pageSize = 5; // default page size

    // Assign paginator for fraud alerts table
    this.fraudAlertsDataSource.paginator = this.fraudAlertsPaginator;
    this.fraudAlertsPaginator.pageSize = 5; // default page size
  }

  loadTransactions(): void {
    this.analyticsService.getTransactions(this.days).subscribe({
      next: data => {
        console.log('Transactions received:', data.transactions);
        this.transactions = data.transactions;
        // Update data source with a new array reference
        this.dataSource.data = [...this.transactions];
        this.transactionsErrorMessage = '';
        // Force change detection to update the paginator length
        this.cdRef.detectChanges();
      },
      error: err => {
        console.error(err);
        this.transactionsErrorMessage = 'Failed to load transactions. Please try again later.';
      }
    });
  }

  loadFraudAlerts(): void {
    this.analyticsService.getFraudAlerts().subscribe({
      next: data => {
        console.log('Fraud alerts received:', data.fraud_alerts);
        this.fraudAlerts = data.fraud_alerts;
        // Update fraud alerts data source with a new array reference
        this.fraudAlertsDataSource.data = [...this.fraudAlerts];
        this.fraudAlertsErrorMessage = '';
        this.cdRef.detectChanges();
      },
      error: err => {
        console.error(err);
        this.fraudAlertsErrorMessage = 'Failed to load fraud alerts. Please try again later.';
      }
    });
  }
}
