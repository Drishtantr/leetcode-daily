function analyzeSurvey(data) {
  // Group engagement scores by department
  const departmentScores = {};
  data.forEach((entry) => {
    if (!departmentScores[entry.department]) {
      departmentScores[entry.department] = [];
    }
    departmentScores[entry.department].push(entry.engagement_score);
  });

  // Calculate average engagement scores for each department
  const engagementScores = {};
  for (const department in departmentScores) {
    const scores = departmentScores[department];
    const average = scores.reduce((a, b) => a + b, 0) / scores.length;
    engagementScores[department] = average;
  }

  // Identify department with highest and lowest engagement
  let highestEngagement = null,
    lowestEngagement = null;
  for (const department in engagementScores) {
    if (
      highestEngagement === null ||
      engagementScores[department] > engagementScores[highestEngagement]
    ) {
      highestEngagement = department;
    }
    if (
      lowestEngagement === null ||
      engagementScores[department] < engagementScores[lowestEngagement]
    ) {
      lowestEngagement = department;
    }
  }

  return {
    engagementScores,
    highestEngagement,
    lowestEngagement,
  };
}

// Example usage
const surveyData = [
  { employee_id: 1, department: "HR", engagement_score: 8 },
  { employee_id: 2, department: "Engineering", engagement_score: 7 },
  { employee_id: 3, department: "HR", engagement_score: 6 },
  { employee_id: 4, department: "Engineering", engagement_score: 9 },
];
console.log(analyzeSurvey(surveyData));
