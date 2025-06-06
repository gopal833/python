// =====================================================================
// Global/General Declarations for the Business Component Script
// Place these functions in the (General) (Declarations) section.
// =====================================================================

/**
 * Checks if a given year is a leap year.
 * @param {number} year - The year to check.
 * @returns {boolean} True if it's a leap year, false otherwise.
 */
function IsLeapYear(year) {
    // Leap year rules: Divisible by 4, unless it's divisible by 100 but not by 400.
    return ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);
}

/**
 * Calculates the absolute difference in days between two date strings,
 * rounded up to the nearest whole day.
 * Throws a Siebel error if dates are invalid or missing.
 *
 * @param {string} startDateStr - The string representation of the start date.
 * @param {string} endDateStr - The string representation of the end date.
 * @returns {number|null} The rounded-up absolute difference in days, or null if an error occurred.
 */
function CalculateDateDifference(startDateStr, endDateStr) {
    if (!startDateStr || !endDateStr) {
        // Raise error if dates are not provided
        TheApplication().RaiseErrorText("Error: Both Start Date and End Date must be provided for date calculation.");
        return null;
    }

    var dtStartDate = new Date(startDateStr);
    var dtEndDate = new Date(endDateStr);

    // Check if Date objects are valid after parsing
    if (isNaN(dtStartDate.getTime()) || isNaN(dtEndDate.getTime())) {
        TheApplication().RaiseErrorText("Error: Invalid date format for calculation. Please ensure Start Date and End Date are valid dates (e.g., MM/DD/YYYY HH:MM:SS).");
        return null;
    }

    var diffMilliseconds = dtEndDate.getTime() - dtStartDate.getTime();
    var diffDays = diffMilliseconds / (1000 * 60 * 60 * 24);

    // Get the absolute difference and round up to the nearest whole day.
    // This handles cases where endDate might be before startDate, and fractional days.
    var roundedUpAbsDays = Math.ceil(Math.abs(diffDays));

    return roundedUpAbsDays;
}

// =====================================================================
// BusComp_PreSetFieldValue Event Handler
// Place this code within the BusComp_PreSetFieldValue function.
// =====================================================================

function BusComp_PreSetFieldValue (FieldName, FieldValue)
{
    var retVal = ContinueOperation; // Default return value for Pre events

    // Check if the field being set is "End Date"
    if (FieldName == "End Date")
    {
        // For debugging: Log the field and its new value
        util.log("BusComp_PreSetFieldValue: Processing FieldName=" + FieldName + ", FieldValue (new)=" + FieldValue);

        // Activate "Start Date" field to ensure its value is available in the buffer
        // This is crucial if "Start Date" is not always active/visible in the UI.
        this.ActivateField("Start Date");

        // Retrieve the current "Start Date" from the Business Component record
        var startDate = this.GetFieldValue("Start Date");
        // Use FieldValue parameter for the new "End Date" value being set
        var endDate = FieldValue;

        // For debugging: Log the retrieved dates
        util.log("BusComp_PreSetFieldValue: Retrieved Start Date='" + startDate + "', New End Date='" + endDate + "'");

        // Only proceed with validation if both dates have valid values
        if (startDate && endDate)
        {
            // Call the custom function to get the calculated difference (rounded up, absolute)
            var validatedDaysDifference = CalculateDateDifference(startDate, endDate);

            // Check if the calculation was successful (i.e., did not return null due to an error)
            if (validatedDaysDifference !== null)
            {
                // Determine the maximum allowed days based on the End Date's year being a leap year
                var dtEndDateForLeapYearCheck = new Date(endDate);
                var endYear = dtEndDateForLeapYearCheck.getFullYear(); // Get the full year from the End Date

                var maxAllowedDays = 365; // Default max days

                // Use the IsLeapYear helper function
                if (IsLeapYear(endYear)) {
                    maxAllowedDays = 366; // If End Date falls in a leap year, allow 366 days
                    util.log("End Date year (" + endYear + ") is a leap year. Max allowed days set to: " + maxAllowedDays);
                } else {
                    util.log("End Date year (" + endYear + ") is a common year. Max allowed days set to: " + maxAllowedDays);
                }

                // For debugging: Log the calculated difference and max allowed days
                util.log("Calculated Days Difference (rounded up): " + validatedDaysDifference);
                util.log("Maximum Allowed Days: " + maxAllowedDays);

                // Perform the validation check
                if (validatedDaysDifference > maxAllowedDays)
                {
                    // Raise a Siebel error message if the difference exceeds the allowed limit
                    TheApplication().RaiseErrorText("End Date cannot be set more than " + maxAllowedDays + " days from the Start Date. Current difference: " + validatedDaysDifference + " days.");
                    retVal = CancelOperation; // Prevent the field from being set and the record from being saved
                } else {
                    util.log("Date difference is within allowed limits (" + validatedDaysDifference + " <= " + maxAllowedDays + ").");
                }
            } else {
                // This block is for cases where CalculateDateDifference returned null (e.g., due to invalid date format).
                // The error message is already raised within CalculateDateDifference itself in such cases.
                util.log("CalculateDateDifference returned null. An error message should have been raised.");
            }
        } else {
            // This block executes if either Start Date or End Date (FieldValue) is empty/null.
            // No validation is performed if dates are not complete.
            util.log("Validation skipped: Start Date or End Date (FieldValue) is missing. Start Date='" + startDate + "', End Date='" + endDate + "'");
        }
    }

    // Always return the operation status at the end of the event handler
    return retVal;
}


