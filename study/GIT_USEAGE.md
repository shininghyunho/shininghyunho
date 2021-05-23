평소 git을 gui로만 사용해서 cli로 써보기위해 찾아봄.

## 명령어
- commit

  일종의 스냅샷. 코드를 add하고 commit 하면 새로운 버전의 스냅샷이 생성됨.

  ex) git commit -m 'commit exaplain'

- branch
	
	특정 커밋에 대한 참조. 많이 만들어도 디스크나 메모리 공간에 부담이 되지않음. 매번 새로운 기능을 만들때 항상 branch를 여러개 만드는게 중요.
	
	ex) git branch branchName (브랜치 생성), branch - f foo c3 (foo브랜치를 c3로 이동)
	
- merge
	
	두 브랜치를 합침.
	
	ex) git merge foo (HEAD에 해당하는 브랜치와 foo 브랜치를 함침)
	
- rebase
	
	base를 새롭게 둠. commit을 새로운 commit 아래에서 새롭게 시작함.
	
	ex) git rebase main (현재 커밋을 main 아래에 복사해둠)
	
- checkout
	
	커밋을 이동함
	
	ex) git checkout foo (foo 브랜치로 이동)
	
- cherry-pick
	
	이름같이 체리처럼 행동함. 자기 아래로 다른 커밋들을 복사해 가져옴. rebase 대신해 사용가능.
	
	ex) git cherry-pick c1 c2 c3 (c1,c2,c3 커밋을 복사해와 붙여줌)
	
- reset
	
	로컬 환경에서 HEAD에 해당하는 작업을 특정 커밋으로 되돌림. 애초에 커밋하지 않은 것처럼 작업함.
	
	ex) git reset c1 (현재 HEAD 커밋을 c1으로 되돌림)
	
- revert
	
	원격 환경에서 사용됨. 특정 작업을 되돌리는데 변경사항을 원래대로 되돌리고 복사본을 commit함
	
	ex) git revert c2 (c2`이 새로 커밋됨) 
### 로그확인
- log

  ex) git log --graph (구체적 커밋 내역을 그래프로 확인)

  ex) git log --graph --oneline --all (커밋 내역을 한줄로 확인)

## 참고
- [git 브랜치 시뮬레이터](https://learngitbranching.js.org/?locale=ko)

