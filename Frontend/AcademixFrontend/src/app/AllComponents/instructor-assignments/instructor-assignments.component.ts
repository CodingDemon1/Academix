import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { iAssignment } from './iAssignment';
import { AssignmentService } from 'src/app/i-assignment.service';

@Component({
  selector: 'app-instructor-assignments',
  templateUrl: './instructor-assignments.component.html',
  styleUrls: ['./instructor-assignments.component.css']
})
export class InstructorAssignmentsComponent implements OnInit {
  courseId!: number;
  assignments: iAssignment[] = [];
  addAssignmentModalVisible: boolean = false;
  updateAssignmentModalVisible: boolean = false;

  constructor(private route: ActivatedRoute, private router: Router,private assignmentService: AssignmentService) {}

  ngOnInit(): void {
    // Fetch the courseId from route parameters
    this.route.params.subscribe(params => {
      this.courseId = params['cId'];
      console.log(this.courseId)
      // Use the courseId to fetch assignments for this course
      // Assignments fetching logic here, e.g., call a service to fetch assignments
      this.loadAssignments(this.courseId)
    });
  }

  // Method to open the "Add Assignment" modal
  openAddAssignmentModal() {
    this.addAssignmentModalVisible = true;
    // You can implement any logic to prepare the modal for adding assignments
  }

  // Method to close the "Add Assignment" modal
  closeAddAssignmentModal() {
    this.addAssignmentModalVisible = false;
    // Reset any form fields or data used for adding assignments
  }

  // Method to open the "Update Assignment" modal
  openUpdateAssignmentModal() {
    this.updateAssignmentModalVisible = true;
  }

  // Method to close the "Update Assignment" modal
  closeUpdateAssignmentModal() {
    this.updateAssignmentModalVisible = false;
    // You can implement logic to close the "Update Assignment" modal
  }

  // Method to delete an assignment
  deleteAssignment(assignmentId: number) {
    this.assignmentService.deleteAssignment(assignmentId).subscribe(
      (res:any)=>{
        if(res.response){
          alert(res.message)
          this.loadAssignments(this.courseId)

        }
      },
        (err:any) =>{
          alert(err)
        }
    )
  }

  // Method to handle adding a new assignment
  addAssignment(newAssignment: iAssignment) {  
    console.log(newAssignment)
    this.assignmentService.createAssignment(newAssignment).subscribe(
      (res)=>{
        if(res.response){
            alert(res.message)
            this.closeAddAssignmentModal()
            this.loadAssignments(this.courseId)
          }
        },
        (err)=>{
          console.log(err)
        }
        )
  }

  updateAssignment(assignment: iAssignment, assignmentId:number){
    assignment['course_id'] = this.courseId
    this.assignmentService.updateAssignment(assignmentId,assignment).subscribe(
      (res:any)=>{
        if(res.response){
            alert(res.message)
            this.closeUpdateAssignmentModal()
            this.loadAssignments(this.courseId)
          }
        },
        (err:any)=>{
          console.log(err)
        }
        )
  }

  loadAssignments(cId:number){
    this.assignmentService.getAssignmentsByCourseId(cId).subscribe(
            (res : any)=>{
              console.log(res)
              if(res.response){
                this.assignments = res.assignment
              }
            },
            (err : any)=>{
              console.log(err)
            } 
          )
  }

}