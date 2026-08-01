class ApprovalGate:


    def check(self, remediation_decision):


        approval = {

            "approved": False,

            "reason": "",

            "action": remediation_decision.get(
                "action"
            )

        }


        if not remediation_decision:

            approval["reason"] = (
                "No remediation decision available"
            )

            return approval



        if remediation_decision.get(
            "approval_required"
        ):

            approval["approved"] = False

            approval["reason"] = (
                "Waiting for human approval"
            )

        else:

            approval["approved"] = True

            approval["reason"] = (
                "Automatic execution allowed"
            )


        return approval