import { TestBed } from '@angular/core/testing';

import { SCoursesService } from './s-courses.service';

describe('SCoursesService', () => {
  let service: SCoursesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SCoursesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
