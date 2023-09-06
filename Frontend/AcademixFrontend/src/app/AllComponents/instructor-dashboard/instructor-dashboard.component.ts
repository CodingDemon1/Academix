import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-instructor-dashboard',
  templateUrl: './instructor-dashboard.component.html',
  styleUrls: ['./instructor-dashboard.component.css']
})
export class InstructorDashboardComponent implements OnInit{

  user !: string | null;

  loggedInUser !: object;
    constructor(private authService: AuthService, private router: Router){}

    ngOnInit(): void {
      this.user = localStorage.getItem("user"); 
      this.loggedInUser = this.authService.getUser()
    }

}
