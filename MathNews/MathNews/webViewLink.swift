//
//  webViewLink.swift
//  MathNews
//
//  Created by Charlie Watson on 3/2/16.
//  Copyright © 2016 cs121MathNewApp. All rights reserved.
//

import UIKit

class webViewLink: UIViewController {

    @IBOutlet weak var webViewer: UIWebView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        webViewer.loadRequest(NSURLRequest(URL: NSURL(string: "google.com")!))
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
