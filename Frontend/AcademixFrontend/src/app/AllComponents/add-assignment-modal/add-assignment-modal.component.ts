import { Component, Input } from '@angular/core';
import { InstructorAssignmentsComponent } from '../instructor-assignments/instructor-assignments.component';
import { AuthService } from 'src/app/auth.service';
import { iAssignment } from '../instructor-assignments/iAssignment';

@Component({
  selector: 'app-add-assignment-modal',
  templateUrl: './add-assignment-modal.component.html',
  styleUrls: ['./add-assignment-modal.component.css']
})
export class AddAssignmentModalComponent {
  @Input() visible: boolean = false;
  @Input() newAssignment: iAssignment = new iAssignment(); // Input for the new course data
  modalVisible : boolean = false;
  user!: any;
  course!:any;
  constructor(private insAssgn : InstructorAssignmentsComponent, private authService: AuthService ) {}

  closeModal() 
  {
    this.insAssgn.closeAddAssignmentModal()
  }

  saveAssignment() {
    this.user  = this.authService.getUser()
    this.course = this.insAssgn.courseId
    this.newAssignment.course_id = this.course
    this.insAssgn.addAssignment(this.newAssignment)
  }

}
