<?php
namespace Home\Controller;

use Think\Controller;
use Home\Model\Captcha;
/**
 * user contrl 
 */
class UserController extends Controller
{
    public function index(){
        if(!session('?logined')){
            $this->show();
        }else{
            $this->success('you success login!',U('index/index'));
        }
            

    }



    public funtion register(){
        if(IS_POST){
            $User=D('user');
            $data['username']=trim(I('post.userName'));
            $data['email']=trim(I('post.email'));
            $data['password']=trim(I('post.password'));
            $data['confirpwd']=trim(I('post.confirmPwd'));
            $data['gender']=trim(I('post.gender'));
            $data['birthday']=trim(I('post.birthday'));
            $data['impath']="/Public/home/imgs/defaultx.png";

            if($User->create($data)){
                if($User->add()){
                    $this->success('reg success,please login!','login');
                }else{
                    $this->error($User->getError());
                }
            }else{
                $this->error($User->getError());
            }
        }else{
            $this->redirect('index',0);
        }
                

    }
}

