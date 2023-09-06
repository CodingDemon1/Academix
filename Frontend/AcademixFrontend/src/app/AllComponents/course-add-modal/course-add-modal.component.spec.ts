import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CourseAddModalComponent } from './course-add-modal.component';

describe('CourseAddModalComponent', () => {
  let component: CourseAddModalComponent;
  let fixture: ComponentFixture<CourseAddModalComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CourseAddModalComponent]
    });
    fixture = TestBed.createComponent(CourseAddModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
