import * as fs from 'fs';

function transformedData(data) {
    
const transformedData = data.data.problemsetQuestionList.questions.map(question => ({
    acRate: question.acRate,
    difficulty: question.difficulty,
    freqBar: question.freqBar,
    frontendQuestionId: question.frontendQuestionId,
    isFavor: question.isFavor,
    paidOnly: question.paidOnly,
    status: question.status,
    title: question.title,
    link: `https://leetcode.com/problems/${question.titleSlug}/description/`,
    topicTags: question.topicTags.map(tag => tag.name)
}));
const headers = [
    "acRate",
    "difficulty",
    "freqBar",
    "frontendQuestionId",
    "isFavor",
    "paidOnly",
    "status",
    "title",
    "link",
    "topicTags"
];

const csvRows = [
    headers.join(","),
    ...transformedData.map(row => headers.map(header => JSON.stringify(row[header] || "")).join(","))
];

const csvContent = csvRows.join("\n");

fs.writeFileSync('output.csv', csvContent);

console.log('CSV file created successfully.');