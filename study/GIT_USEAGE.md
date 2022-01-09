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
	
	remote branch를 checkout 하는 방법 : git checkout -t origin/branchname
	
- cherry-pick
	
	이름같이 체리처럼 행동함. 자기 아래로 다른 커밋들을 복사해 가져옴. rebase 대신해 사용가능.
	
	ex) git cherry-pick c1 c2 c3 (c1,c2,c3 커밋을 복사해와 붙여줌)
	
- reset
	
	로컬 환경에서 HEAD에 해당하는 작업을 특정 커밋으로 되돌림. 애초에 커밋하지 않은 것처럼 작업함.
	
	ex) git reset c1 (현재 HEAD 커밋을 c1으로 되돌림)
	
- revert

  원격 환경에서 사용됨. 특정 작업을 되돌리는데 변경사항을 원래대로 되돌리고 복사본을 commit함

  ex) git revert c2 (c2`이 새로 커밋됨) 

- fetch

  원격으로부터 로컬 환경을 동기화시킴.

  원격 저장소에는 있지만 로컬에는 없는 커밋들을 다운받아오고, 로컬에 원격 브랜치가 가리키는 곳을 업데이트함(origin/main 같은)

  그러나 로컬 환경을 변경시키지는 않음. 그래서 현재 작업중이라면 fetch가 안전함.

- pull

  git fetch + git merge origin/main. 가져와서 바로 머지시킴.

  ex) git pull

  merge 대신 rebase를 하고싶으면

  ex) git pull --rebase

- push

  로컬 환경을 원격 환경에 동기화 시킴.

  ':'을 명시하면 방향성을 표시할 수도 있음. 

  ex) git push origin main (origin(원격) 에 main(로컬) 브랜치를 동기화해줌)
### 로그확인
- log

  ex) git log --graph (구체적 커밋 내역을 그래프로 확인)

  ex) git log --graph --oneline --all (커밋 내역을 한줄로 확인)

### GIT Repo 최조 생성시

#### 로컬 환경이 없을때

`echo "# jpabook_for_study" >> README.md` // readme 생성

`git init` // 초기화

`git add README.md` // readmd stage

`git commit -m "first commit"` // commit

`git branch -M main` // 현재 브랜치를 매인으로 정함

`git remote add origin https://github.com/shininghyunho/jpabook_for_study.git` // 원격 연결

`git push -u origin main` // 앞으로 git push만 해도 main이 올라감



#### 로컬 환경이 있을때

```
git remote add origin https://github.com/shininghyunho/jpabook_for_study.git
git branch -M main
git push -u origin main
```
---
### github에서 삭제한 branch 가 local에 남아있을때
```
git remote prune origin
```

## 참고
- [git 브랜치 시뮬레이터](https://learngitbranching.js.org/?locale=ko)

