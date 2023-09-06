import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  userRole: string |null = ''; // Store the user's role (student or instructor)

  constructor(private route: ActivatedRoute, private userService: UserService) { }

  ngOnInit(): void {
    // Get the user's role from the route parameter (you can obtain it from your authentication logic)
    this.userRole = localStorage.getItem("loggedUserRole")
    // this.userRole = this.userService.getUserRole();
  }
}
