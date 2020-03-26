HomePageMap = dict(AboutMeXpath='//*[@id="navbar-collapse"]/ul[1]/li[2]/a[1]',
                   WorkXpath='//*[@id="navbar-collapse"]/ul[1]/li[3]/a[1]',
                   TalksXpath='//*[@id="navbar-collapse"]/ul[1]/li[4]/a[1]',
                   LinkedInXpath='//*[@id="navbar-collapse"]/ul[1]/li[5]/a[1]'

                   )

ContactPageMap = dict(FirstNameFieldXpath="//input[contains(@name, 'first')]",
                      LastNameFieldXpath="//input[contains(@name, 'last')]",
                      EmailFieldXpath="(//input[contains(@id, 'input')])[3]",
                      CommentFieldXpath="//textarea",
                      SubmitButtonXpath="//span[.='Submit']",
                      ThankYouMessageXpath="//div[contains(text(), 'Thank you')]"

                      )
