import Vue from 'vue'
import Router from 'vue-router'
import Cabinet from '@/components/Cabinet'
import CabinetIssues from '@/components/CabinetIssues'
import CabinetProfile from '@/components/CabinetProfile'
import Issue from '@/components/Issue'
import IssueSurvey from '@/components/IssueSurvey'
import IssueDocuments from '@/components/IssueDocuments'
import IssueSecurityManagement from '@/components/IssueSecurityManagement'
import IssueLawyersManagement from '@/components/IssueLawyersManagement'
import IssueDocOpsManagement from '@/components/IssueDocOpsManagement'
import IssueMessaging from '@/components/IssueMessaging'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/cabinet/issues'
    },
    {
      path: '/cabinet',
      name: 'cabinet',
      component: Cabinet,
      redirect: '/cabinet/issues',
      children: [
        {
          path: 'issues',
          name: 'issues',
          component: CabinetIssues
        },
        {
          path: 'profile',
          name: 'profile',
          component: CabinetProfile
        }
      ]
    },
    {
      path: '/cabinet/issues/:id',
      redirect: '/cabinet/issues/:id/info'
    },
    {
      path: '/cabinet/issues/:id/info',
      name: 'issue-info',
      component: Issue
    },
    {
      path: '/cabinet/issues/:id/survey',
      name: 'issue-survey',
      component: IssueSurvey
    },
    {
      path: '/cabinet/issues/:id/documents',
      name: 'issue-documents',
      component: IssueDocuments
    },
    {
      path: '/cabinet/issues/:id/security-mgmt',
      name: 'issue-security-mgmt',
      component: IssueSecurityManagement
    },
    {
      path: '/cabinet/issues/:id/lawyers-mgmt',
      name: 'issue-lawyers-mgmt',
      component: IssueLawyersManagement
    },
    {
      path: '/cabinet/issues/:id/doc-ops-mgmt',
      name: 'issue-doc-ops-mgmt',
      component: IssueDocOpsManagement
    },
    {
      path: '/cabinet/issues/:id/messaging',
      name: 'issue-messaging',
      component: IssueMessaging
    }
  ]
})
