Feature: Baidu search test case

Scenario: search selenium
Given I go to "http://www.baidu.com/"
When I fill in field with id "kw" with "selenium"
And I click id "su" with baidu once
Then I should see "selenium_百度搜索" within 2 second