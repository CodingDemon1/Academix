import { TestBed } from '@angular/core/testing';

import { ICourseService } from './i-course.service';

describe('ICourseService', () => {
  let service: ICourseService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ICourseService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
