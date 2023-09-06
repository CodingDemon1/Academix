import { TestBed } from '@angular/core/testing';

import { SAssignmentService } from './s-assignment.service';

describe('SAssignmentService', () => {
  let service: SAssignmentService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SAssignmentService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
