import { Component } from '@angular/core';
import { SAssignmentService } from 'src/app/s-assignment.service';
import { Assignment } from './assignment.model';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-student-assignments',
  templateUrl: './student-assignments.component.html',
  styleUrls: ['./student-assignments.component.css']
})
export class StudentAssignmentsComponent {
  assignments: Assignment[] = [];
  sID !: number;

  constructor(private assignmentService: SAssignmentService, private authService : AuthService) {}

  ngOnInit(): void {
    this.sID = this.authService.getUser().id;

    this.loadAssignments(this.sID)
    
  }

  loadAssignments(sID: number){
    this.assignmentService.getAssignmentsByStudentId(sID).subscribe(
      (res: any) => {
        this.assignments = res.assignments;
        },
      (err: any)=>{
        console.log(err)
      }
    );
  }
}
