import unittest
import coverage
# Start code coverage measurement
cov = coverage.Coverage()
cov.start()
# Discover and load all the tests from the 'tests' folder
test_loader = unittest.TestLoader()
test_suite = test_loader.discover('tests', pattern='*.py')
# Run the tests and display the results
test_runner = unittest.TextTestRunner(verbosity=2)
test_result = test_runner.run(test_suite)
# Stop code coverage measurement
cov.stop()
# Save coverage data to .coverage file
cov.save()
# Generate code coverage report
cov.report()
# Optionally, you can also generate an HTML report
cov.html_report(directory='coverage_html')
# Load the coverage data from the .coverage file
cov.load()
