import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateAssignmentModalComponent } from './update-assignment-modal.component';

describe('UpdateAssignmentModalComponent', () => {
  let component: UpdateAssignmentModalComponent;
  let fixture: ComponentFixture<UpdateAssignmentModalComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UpdateAssignmentModalComponent]
    });
    fixture = TestBed.createComponent(UpdateAssignmentModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
