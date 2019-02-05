//
//  ViewController.swift
//  SafeFace
//
//  Created by Mohammadreza on 2/3/19.
//  Copyright © 2019 Mark Mohades. All rights reserved.
//

import UIKit
import Alamofire

class ViewController: UIViewController {

    @IBOutlet weak var lockButton: UIButton!
    @IBOutlet weak var unlockButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()


        
    }
    
    
    
    
    @IBAction func lockPressed(_ sender: Any) {
        
        request(with : "http://10.126.79.15:5000/lock")
        animate(this: lockButton)

    }
    
    
    
    
    @IBAction func unlockPressed(_ sender: Any) {
        
        request(with: "http://10.126.79.15:5000/unlock")
        animate(this: unlockButton)


    }
    
    
    
    func request(with url: String){
    
        
        Alamofire.request(url, method: .get)
            .responseJSON { response in
                if response.result.isSuccess {
                    
                    print("Sucess!")
                    
                
                }
                    
                else {
                    print("Error: \(String(describing: response.result.error))")
                    
                }
        }
        
        
    }
    
    
    
    func animate (this button: UIButton){
        
        UIView.animate(withDuration: 0.6,
                       animations: {
                        button.transform = CGAffineTransform(scaleX: 0.6, y: 0.6)
        },
                       completion: { _ in
                        UIView.animate(withDuration: 0.6) {
                            button.transform = CGAffineTransform.identity
                        }
        })
        
    }
    
    
    override var preferredStatusBarStyle: UIStatusBarStyle {
        return .lightContent
    }


}

