# Statistics

0. Setting the ".bashrc" configure on your home directory like following :
	
	git config --global user.email "your email address"  ("your email address" should be replaced by yours, i.e. skyblue111@naver.com) 
	
	git config --global user.name "your user name"       ("your user name" should be replace by yours on github ID, i.e. junholeephy)

1. "Fork" the "Statistics" repository onto your account

2. Input following command on your terminal :

	(git config --global  credential.usehttppath true  :: in case of push error on Window)	

	git clone https://github.com/StudyGroupPKU/Statistics.git

	git remote add upstream https://github.com/StudyGroupPKU/Statistics.git

	git fetch upstream

	git pull upstream master

3. In order to upload newly added file to your own forked repository :

	(0)	git status    (This is mainly for checking whether the new file is correctly written at the expected directory. )

	(1) git add *filename*  (for example,  "git add test.py"  in order to upload "test.py" )

	(2) git commit -m  "description of the file"

	(3) git push origin 

	(After this, if you want, you can make a pull request for merging your contribution to master branch. This procedure can be done by clicking "pull requtest" button on the github website)

4. If there are some changes on masster branch that you want to update onto your own repository, do following:
	
	(0) git checkout "branch"   ("branch" should be replace by the name of existing branch which we want to update, i.e. junho)

	(1) git fetch upstream

	(2) git pull upstream master

	(3) git push

5. Addtional git command you might interested in :
	git branch -a
	git checkout master (or a branch name)
	git rm tttest.py		(remove a certain file, say tttest.py, from your own repository after commit and push)



