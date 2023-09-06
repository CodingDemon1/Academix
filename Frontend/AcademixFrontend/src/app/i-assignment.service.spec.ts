import { TestBed } from '@angular/core/testing';

import { IAssignmentService } from './i-assignment.service';

describe('IAssignmentService', () => {
  let service: IAssignmentService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(IAssignmentService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
