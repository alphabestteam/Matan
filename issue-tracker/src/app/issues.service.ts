import { Injectable } from '@angular/core';
import { Issues } from './issues';

@Injectable({
  providedIn: 'root'
})
export class IssuesService {
    private issues: Issues[] = [];

    constructor() { }

    getPendingIssues(): Issues[] {
        return this.issues.filter(issue => !issue.completed);
    }

    createIssue(issue: Issues) {
        issue.issueNo = this.issues.length + 1;
        this.issues.push(issue);
    }
}
