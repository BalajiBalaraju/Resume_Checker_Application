// This file contains the JavaScript for the frontend.

document.addEventListener('DOMContentLoaded', () => {
    const jdUpload = document.getElementById('jd-upload');
    const resumeUpload = document.getElementById('resume-upload');
    const analyzeButton = document.getElementById('analyze-button');
    const statusMessage = document.getElementById('status-message');
    const resultsDashboard = document.getElementById('results-dashboard');

    analyzeButton.addEventListener('click', async () => {
        const jdFile = jdUpload.files[0];
        const resumeFile = resumeUpload.files[0];

        if (!jdFile || !resumeFile) {
            showMessageBox('Please upload both a Job Description and a Resume.', 'error');
            return;
        }

        // Show loading status
        statusMessage.classList.remove('hidden');
        resultsDashboard.classList.add('hidden', 'opacity-0');
        analyzeButton.disabled = true;

        const formData = new FormData();
        formData.append('jd', jdFile);
        formData.append('resume', resumeFile);

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok) {
                updateDashboard(data);
            } else {
                showMessageBox(data.error, 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showMessageBox('An error occurred during analysis.', 'error');
        } finally {
            statusMessage.classList.add('hidden');
            analyzeButton.disabled = false;
        }
    });

    function updateDashboard(results) {
        const relevanceScoreDisplay = document.getElementById('relevance-score-display');
        const suitabilityVerdict = document.getElementById('suitability-verdict');
        const missingSkillsList = document.getElementById('missing-skills-list');
        const feedbackText = document.getElementById('feedback-text');

        relevanceScoreDisplay.textContent = results.score;
        suitabilityVerdict.textContent = results.verdict;

        suitabilityVerdict.classList.remove('text-green-600', 'text-yellow-600', 'text-red-600');
        if (results.score > 80) {
            suitabilityVerdict.classList.add('text-green-600');
        } else if (results.score > 60) {
            suitabilityVerdict.classList.add('text-yellow-600');
        } else {
            suitabilityVerdict.classList.add('text-red-600');
        }

        missingSkillsList.innerHTML = '';
        results.missing_skills.forEach(skill => {
            const li = document.createElement('li');
            li.textContent = skill;
            missingSkillsList.appendChild(li);
        });

        feedbackText.textContent = results.feedback;

        resultsDashboard.classList.remove('hidden');
        setTimeout(() => {
            resultsDashboard.classList.remove('opacity-0');
        }, 50);
    }

    function showMessageBox(message, type) {
        const messageBox = document.createElement('div');
        messageBox.className = `fixed bottom-4 left-1/2 -translate-x-1/2 px-6 py-3 rounded-full text-white font-semibold shadow-lg transition-all duration-300 transform scale-0 opacity-0 z-50`;
        
        if (type === 'error') {
            messageBox.classList.add('bg-red-500');
        } else {
            messageBox.classList.add('bg-gray-800');
        }

        messageBox.textContent = message;
        document.body.appendChild(messageBox);
        
        setTimeout(() => {
            messageBox.classList.remove('scale-0', 'opacity-0');
            messageBox.classList.add('scale-100', 'opacity-100');
        }, 50);

        setTimeout(() => {
            messageBox.classList.remove('scale-100', 'opacity-100');
            messageBox.classList.add('scale-0', 'opacity-0');
            setTimeout(() => messageBox.remove(), 300);
        }, 3000);
    }
});