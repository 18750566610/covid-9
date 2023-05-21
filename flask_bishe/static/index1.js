try{
    PIXI.resolution = 2;
            //添加画布/舞台
            var app = new PIXI.Application(512,768);
            document.body.appendChild(app.view);
    
            //所需参数
            var type = 0;
            var fen = 0;
            var hp = 10;
            var hpMax = 10;
    
            //创建背景对象
            var bg = new PIXI.Sprite.fromImage("res/plane/bg/img_bg_level_3.jpg");
            app.stage.addChild(bg);
    
            //创建云对象，设置云所在画布的坐标
            var yun = new PIXI.Sprite.fromImage("res/texiao/yun02.png");
            app.stage.addChild(yun);
            yun.x = 20;
            yun.y = 130;
    
            //飞机动画，设置动画速度为0.1秒一张图片
            var alienImages = ["res/plane/plays/planplay_1.png","res/plane/plays/planplay_2.png","res/plane/plays/planplay_3.png","res/plane/plays/planplay_4.png","res/plane/plays/planplay_5.png","res/plane/plays/planplay_6.png","res/plane/plays/planplay_7.png","res/plane/plays/planplay_8.png","res/plane/plays/planplay_9.png","res/plane/plays/planplay_10.png","res/plane/plays/planplay_11.png"];
    
            var plane = PIXI.extras.AnimatedSprite.fromImages(alienImages);
            app.stage.addChild(plane);
            plane.animationSpeed = 0.1;
    
            plane.x = 200;
            plane.y = 550;
    
            //设置飞机锚点
            plane.anchor.x = 0.5;
            plane.anchor.y = 0.5;
    
            //添加僚机
            //僚机左
            var planeLeft = new PIXI.Sprite.fromImage("res/plane/liaoji_02_11.png");
            plane.addChild(planeLeft);
            planeLeft.anchor.x = 0.5;
            planeLeft.anchor.y = 0.5;
            planeLeft.x = 80;
            planeLeft.y = 50;
    
            //僚机右
            var planeRight = new PIXI.Sprite.fromImage("res/plane/liaoji_02_11.png");
            plane.addChild(planeRight);
            planeRight.anchor.x = 0.5;
            planeRight.anchor.y = 0.5;
            planeRight.x = -80;
            planeRight.y = 50;
    
            //得分模块
            var defen = new PIXI.Text("得分：00000");
            defen.style.fill = "0xffffff";
            app.stage.addChild(defen);
            defen.x = 310;
            defen.y = 10;
            //飞机总血条
            //由两个图层，一个图层是黑的，一个红的，扣血就会显示出黑的，表示扣血
            var hpBg = new PIXI.Sprite.fromImage("res/plane/ui/2_03.png");
            app.stage.addChild(hpBg);
            hpBg.y = 14;
    
            var hpTiao = new PIXI.Sprite.fromImage("res/plane/ui/3_03.png");
            app.stage.addChild(hpTiao);
            hpTiao.x = 33;
            hpTiao.y = 14;
            
            var hpPic = new PIXI.Sprite.fromImage("res/plane/ui/img_ui_16.png");
            app.stage.addChild(hpPic);
            hpPic.x = 10;
            hpPic.y = 12;
    
            var item = new PIXI.Sprite.fromImage("res/plane/item/img_plane_item_15.png");
            app.stage.addChild(item);
            item.x = 100;
            item.y = 200;
            item.anchor.x = 0.5;
            item.anchor.y = 0.5;
    
            // //控制飞机
            bg.interactive = true;
            bg.on("mousemove", planeMove);
    
            function planeMove(event) {
                if(type == 0) {
                    return;
                }
                var pos = event.data.getLocalPosition(app.stage);
                plane.x = pos.x;
                plane.y = pos.y;
            }
    
            //暂停
            var pauseBtn = new PIXI.Sprite.fromImage("res/plane/ui/ui_new_btn_png_03.png");
            app.stage.addChild(pauseBtn);
            pauseBtn.x = 460;
            pauseBtn.y = 10;
            pauseBtn.visible = false;
    
            //继续游戏
            var continueBtn = new PIXI.Sprite.fromImage("res/plane/ui/start.png");
            app.stage.addChild(continueBtn);
            continueBtn.y = 30;

            //暂停按钮事件，点击暂停即触发，使用on（）回调函数pause
            pauseBtn.interactive = true;
            pauseBtn.on("click", pause);
            function pause() {
                type = 0;
                continueBtn.visible = true;
                pauseBtn.visible = false;
                plane.stop();
            }

            //游戏开始事件，点击游戏开始按钮播放飞机动画，使用on（）回调函数jixu
            continueBtn.interactive = true;
            continueBtn.on("click", jixu);
            function jixu() {
                type = 1;
                continueBtn.visible = false;
                pauseBtn.visible = true;
                plane.play();
            }
    
            //gameover游戏结束事件
            var gameoverBtn = new PIXI.Sprite.fromImage("res/plane/ui/gameover.png");
            //gameoverBtn.visible = false;
    
            gameoverBtn.interactive = true;
            gameoverBtn.on("click", restart);
            function restart() {
                window.location.reload();
            }
            //发射子弹
            var bulletSpeed = 10;
            var bulletSubTime = 10;
            var bulletArr = [];
            var fireTime = 10;
            function fire(){
                if(fireTime == 0) {
                    var bullet = new PIXI.Sprite.fromImage("res/plane/bullet_02.png");
                    app.stage.addChild(bullet);
    
                    bullet.anchor.x = 0.5;
                    bullet.anchor.y = 0.5;
                    bullet.x = plane.x;
                    bullet.y = plane.y - 100;
                    
                    bulletArr.push(bullet);
                    fireTime = bulletSubTime;
                }
                fireTime --;
            }

            //添加多敌机
            var enemyArr = [];
            var enemyTime = 30;
            function addEnemy() {
                if(enemyTime == 0) {
                    var enemy = new Enemy();
                    enemy.init();
                    enemyArr.push(enemy);
                    enemyTime = 30;
                }
    
                enemyTime --;
            }
    
            //添加敌机子弹
            var enemyBulletArr = [];
            function addEnemyBullet(x, y) {
                var bullet = new EnemyBullet();
                bullet.init(x, y);
                enemyBulletArr.push(bullet);
            }
    
            function animate() {
    
                if(type == 0) {
                    return;
                }
                //发射子弹
                fire();
                //添加敌机
                addEnemy();
    
                //背景移动
                bg.y += 1;
                if(bg.y > 0) {
                    bg.y = -768;
                }
    
                //云彩移动
                yun.y += 1.5;
                if(yun.y > 800){
                    yun.y = - 400;
                }
                //子弹移动
                for(var i = bulletArr.length - 1; i >= 0; i --){
                    var bullet = bulletArr[i];
                    bullet.y -= bulletSpeed;
                    if(bullet.y < -100) {
                        //子弹销毁
                        app.stage.removeChild(bullet);
                        bulletArr.splice(i, 1);
                    }
                } 
                //敌机移动
                for(var i = enemyArr.length - 1; i >= 0; i --){
                    var enemy = enemyArr[i];
                    enemy.action();
                    if(enemy.plane.y > 800) {
                        //销毁飞机
                        enemy.destory();
                        enemyArr.splice(i, 1);
                    }
                }
    
                //碰撞判断
                for(var j = bulletArr.length - 1; j >= 0; j --) {
                    var bullet = bulletArr[j];
                    for(var i = enemyArr.length - 1; i >= 0 ; i --) {
                       var enemy = enemyArr[i].plane;
                       var pos = (bullet.x - enemy.x) * (bullet.x - enemy.x) + (bullet.y - enemy.y) * (bullet.y - enemy.y);
                       if(pos < 60 * 60) {//碰撞
                            //子弹销毁
                            app.stage.removeChild(bullet);
                            bulletArr.splice(j, 1);
                            //销毁飞机
                            if(enemyArr[i].crash() == true) {
                                enemyArr.splice(i, 1);
                            }
                        
                            //得分
                            fen += 200;
                            defen.text = "得分：" + fen;
                            break;
                        }
                    }
                }
    
                //道具移动
                item.x += 0.5;
                item.y += 2;
                if(item.y > 800) {
                    item.y = - 200;
                }
                if(item.x > 560) {
                    item.x = -50;
                }
    
                //碰撞道具
                var xx = plane.x - item.x;
                var yy = plane.y - item.y;
                if(xx * xx + yy * yy < 50 * 50) {
                    bulletSpeed += 4;
                    bulletSubTime -= 15;
                    if(bulletSubTime < 5) {
                        bulletSubTime = 5;
                    }
                    item.y = - 500;
                }
    
                //敌机子弹移动
                for(var i = enemyBulletArr.length - 1; i >= 0; i --) {
                    var enemyBullet = enemyBulletArr[i];
                    enemyBullet.action();
    
                    if(enemyBullet.image.y > 800) {
                        enemyBullet.remove();
                        enemyBulletArr.splice(i, 1);
                    }
                }
    
                //子弹与玩家飞机碰撞
                for(var i = enemyBulletArr.length - 1; i >= 0; i --) {
                    var enemyBullet = enemyBulletArr[i];
                    
                    var pos = (enemyBullet.image.x - plane.x) * (enemyBullet.image.x - plane.x) + (enemyBullet.image.y - plane.y) * (enemyBullet.image.y - plane.y);
                    if(pos < 40 * 40) {//碰撞
                        hp --;
                        hpTiao.scale.x = hp/hpMax;
    
                        //子弹销毁
                        enemyBullet.remove();
                        enemyBulletArr.splice(i, 1);
    
                        if(hp == 0) {
                            //gameover
                            type = 0;
                            plane.stop();
                            gameoverBtn.visible = true;
                            app.stage.addChild(gameoverBtn);
                        }
                    }
                 }
                    
            }
            app.ticker.add(animate);
    
    
            /* 
            #######################
                创建敌机对象
            ######################
            */
            function Enemy() {
                this.plane = null;
                this.speed = 0;
    
                this.fireTime = 50;
                this.fireSubTime = 200;
    
                this.hpBg;//血条背景
                this.hpTiao;//血条
                this.hp = 3;//血量
                this.hpAll = 3;//满血
                
                this.init = function() {
                    
                    var type = parseInt(Math.random() * 3);
                    this.speed = Math.random() * 3 + 2;
                    
                    var img = "res/plane/enemy_04.png";
                    if(type == 1) {
                        img = "res/plane/enemy_03.png";
                    } else if(type == 2){
                        img = "res/plane/enemy_02.png";
                    }
                    
                    this.plane = new PIXI.Sprite.fromImage(img);
                    //将plane添加到舞台（stage）中
                    app.stage.addChild(this.plane);
                    this.plane.x = Math.random() * 450 + 50;
                    //设置中心点
                    this.plane.anchor.set(0.5,0.5);
    
                    //添加血条
                    this.hpBg = PIXI.Sprite.fromImage("res/plane/item/img_plane_boss_02.png");
                    this.hpFr = PIXI.Sprite.fromImage("res/plane/item/img_plane_boss_05.png");
                    this.plane.addChild(this.hpBg);
                    this.plane.addChild(this.hpFr);
                    this.hpFr.x = -40;
                    this.hpBg.x = -40;
                    this.hpFr.y = -40;
                    this.hpBg.y = -40;
    
                    this.hpFr.scale.x = 0.3;
                    this.hpFr.scale.y = 0.3;
                    this.hpBg.scale.x = 0.3;
                    this.hpBg.scale.y = 0.3;
                }
            
                this.action = function() {
                    this.move();
                    this.fire();
                }
    
                this.move = function() {
                    this.plane.y += this.speed;
                }
    
                this.fire = function() {
                    if(this.fireTime <= 0) {
                        addEnemyBullet(this.plane.x, this.plane.y);
                        this.fireTime = this.fireSubTime;
                    }
                    this.fireTime --;
                }
    
                this.crash = function() {
                    //碰撞
                    this.hp -= 1;
                    this.hpFr.scale.x = this.hp/this.hpAll * 0.3;
                    if(this.hp <= 0) {
                        this.destory();
                        return true;
                    }
                    return false;
                }
    
                this.destory = function() {
                    this.plane.parent.removeChild(this.plane);
                }
            }
    
            /* 
            #######################
                创建子弹对象
            ######################
            */
            function EnemyBullet() {
                
                this.image;
                this.drectionX = 0;
                this.drectionY = 0;
                this.speed = 10;
                
                this.init = function(x, y) {
                    
                    this.image = new PIXI.Sprite.fromImage("res/plane/bullet/img_bullet_17.png");
                    this.image.x = x;
                    this.image.y = y;
                    //设置中心点
                    this.image.anchor.x = 0.5;
                    this.image.anchor.y = 0.5;
                    
                    var t = Math.atan((plane.x - this.image.x) / (plane.y - this.image.y));
                    //console.log(t);
                    this.drectionX = Math.cos(t) * this.speed;
                    this.drectionY = Math.sin(t) * this.speed;
                    if(this.image.y > plane.y) {
                        this.drectionX = -this.drectionX;
                        this.drectionY = -this.drectionY;
                    }
                
                    app.stage.addChild(this.image);   
                }
                
                this.action = function() {
                    
                    this.move();
                }
                
                this.move = function() {
                    
                    this.image.x += this.drectionY;
                    this.image.y += this.drectionX;
                    
                }
                
                this.remove = function() {
                    app.stage.removeChild(this.image);
                }
            }
    }catch(e){
    }
    
    