import { TestBed } from '@angular/core/testing';

import { FraudAlertsService } from './fraud-alerts.service';

describe('FraudAlertsService', () => {
  let service: FraudAlertsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FraudAlertsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
