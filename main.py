B
    �H�[  �               @   s�   d dl Z d dlZd dlZd dlZd dlZdZdZdZdZdZ	ej�
� Z
e
�d�Zed e e e d	 e	 Zd
d� Zdd� Ze�  dS )�    Nz[93mz[94mz[95mz[96mz[0mz%H:%M:%S�[�]c               C   s(   t �d� t �d� td� td� d S )N�clearz0toilet -f mono12 --filter border:metal 'ARYoume'zCheck Facebook Access Token� )�os�system�print� r	   r	   �main.py�title   s    

r   c        
   
   C   s  t �  ttd �} | dkr�d}tdd�}x�|D ]�}t�d| �}|j}|dkrdttt d | � q.ttt	 d	 | � tdd
��R}|�
� }|�� }|�d� x(|�d�D ]}	|	|kr�|�|	d � q�W |��  W d Q R X q.W nttt	 d � t�  t �  td� ttt d � d S )NzPlease Enter to Start Check� �   z	token.txt�rz+https://graph.facebook.com/me?access_token=��   u   [√] z[X] zr+r   �
zWrong Restart.....r   uj   Done! ระบบได้ลบบ Token ที่เสียออกจากไฟล์แล้ว)r   �input�time�open�requests�getZstatus_coder   �gr   �read�strip�seek�split�write�truncate�main�e)
�start�i�f�tokenZchZtkZcko�tZ	to_delete�liner	   r	   r
   r      s0    


r   )r   r   Zdatetime�sysr   r   r   r   r!   �dZnowZstrftimer#   r   r   r	   r	   r	   r
   �<module>   s   

