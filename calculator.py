n=int(input("enter the first number:"))
m=int(input("enter the second number:"))
operator = input("enter the operator (+, -, *, /): ")
for i in range(1):
    if operator=="+":
            print(n+m,)
    elif operator=="-":
            print(n-m)
    elif operator=="*":
          print(n*m)
    elif operator=="/":
            print(n/m)
    else:
            print("invalid operation")

// Function to calculate the difference in days
function CalculateDateDifference(startDateStr, endDateStr) {
    if (!startDateStr || !endDateStr) {
        // You might consider not raising an error here, but returning null,
        // and letting the calling function decide to raise it.
        // For now, keeping it here as per previous example.
        TheApplication().RaiseErrorText("Error: Both Start Date and End Date must be provided for calculation.");
        return null;
    }

    var dtStartDate = new Date(startDateStr);
    var dtEndDate = new Date(endDateStr);

    if (isNaN(dtStartDate.getTime()) || isNaN(dtEndDate.getTime())) {
        TheApplication().RaiseErrorText("Error: Invalid date format for calculation. Please ensure Start Date and End Date are valid dates (e.g., MM/DD/YYYY HH:MM:SS).");
        return null;
    }

    var diffMilliseconds = dtEndDate.getTime() - dtStartDate.getTime();
    var diffDays = diffMilliseconds / (1000 * 60 * 60 * 24);

    // IMPORTANT: Return the raw, potentially fractional difference.
    // The rounding/ceiling logic will be applied at the point of validation.
    return diffDays;
}

// Your Business Component PreSetFieldValue Event (for 'End Date' field)
function BusComp_PreSetFieldValue (FieldName, FieldValue)
{
    var retVal = ContinueOperation;

    if (FieldName == "End Date")
    {
        var startDate = this.GetFieldValue("Start Date");
        var endDate = FieldValue; // Use FieldValue for the new End Date

        if (startDate && endDate)
        {
            var rawDaysDifference = CalculateDateDifference(startDate, endDate); // Get the raw fractional difference

            if (rawDaysDifference !== null) { // Check if calculation was successful
                // Convert to an absolute value and apply Math.ceil for the validation check
                var validatedDaysDifference = Math.ceil(Math.abs(rawDaysDifference));

                util.log("Calculated rawDaysDifference: " + rawDaysDifference);
                util.log("ValidatedDaysDifference (Math.ceil(Math.abs)): " + validatedDaysDifference);


                if (validatedDaysDifference > 365) { // Now comparing an integer
                    TheApplication().RaiseErrorText("End Date cannot be set more than 365 days from the Start Date. Current difference: " + validatedDaysDifference + " days.");
                    retVal = CancelOperation;
                }
            }
        }
    }

    return retVal;
}

