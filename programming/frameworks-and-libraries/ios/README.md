# iOS

## Human Interface Guidelines
If you are new to mobile development or to iOS itself, take some time to take a look at the [Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/ "Human Interface Guidelines") by Apple. This is how Apple encourages both designers and developers to build their apps. Sticking to the Human Interface Guidelines (commonly referenced as *HIG*) is not optional for us, since it comes a lot of benefits for both the development team and the users. Those guidelines also provide a really good overview of native UI components and capabilities such as 3D Touch, Face/Touch ID or Wallet.

## Xcode
[Xcode](https://developer.apple.com/xcode/) is the IDE of choice for iOS and macOS, and the only one officially supported by Apple. You’re encouraged but not restricted to use it, and you can use some alternatives such as Jetbrains’ [AppCode](https://www.jetbrains.com/objc/).  In order to install Xcode, simply download Xcode on the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835).

## Project Setup
There is a common controversy regarding whether to write the UI in pure code or use storyboards to build it in a more graphical way (drag-and-drop). Both are know to work well depending on the use case and the project size.

There are some considerations to take in account if you use Storyboards:
- Storyboards are more prone to have merge conflicts since they use an internal auto-generated XML structure.
- It’s way easier to structure and reuse views in code, easily avoiding repeated code.
- Using storyboards can cause coupling between your code and the UI, which can lead to crashes (e.g  when an outlet or action is not set up correctly). _These issues are not detected by the compiler_.

Even though using code has it’s advantages, Storyboards can be helpful if you’re new to the ecosystem or want to rapidly layout an interface for an MVP or PoC. Also, iteration is often faster since you can preview most UI changes without rebuilding your project. For size classes (similar to responsive design if you come from the web ecosystem), Interface Builder gives you a live preview of how your interface looks like in all device sizes.

### Using storyboards and code for UI at the same time
You can get the best of both worlds by simply using an hybrid approach. Start sketching the initial design with Storyboards (you can also invite designers to work with you in that step). Then, when you need more reliability on the UI, you may progressively transition to a code-based setup that is easier to maintain.

## Ignores
If you’re using Swift, you need to make _git_ to ignore some files that should not be versioned. Please use [this .gitignore file](https://github.com/github/gitignore/blob/master/Swift.gitignore) provided by GitHub. (An [Objective-C version is also available](https://github.com/github/gitignore/blob/master/Objective-C.gitignore))

## Dependency Management
We usually use **Cocoapods** for dependency management. In order to install it you’ll need to do:  
```bash
sudo gem install cocoapods
```
And create a `Podfile` in your project with
```bash
pod init
```

Then, run a `pod install` , that will create an `.xcworkspace` file that you’ll need to use instead of the `.xcproject` you had used before. If you keep using the project file, Xcode won’t find the external dependencies as they are kept in the `Pods` project inside the workspace.

### Common Libraries
- For networking, use [AlamoFire](https://github.com/Alamofire/Alamofire).
- For date formatting, use [DateTools](https://github.com/MatthewYork/DateTools).
- If you choose to write UI code, do it using [SnapKit](https://github.com/SnapKit/).

## Project Structure
In order to keep all your source code in order, you may want to follow some folder structure depending on your architecture. For instance, you can use the following:
```
├── Project
│   ├── AppDelegate.swift
│   ├── Assets.xcassets
│   ├── Colors.swift
│   ├── Constants.swift
│   ├── Models
│   │   ├── Model1.swift
│   │   ├── Model2.swift
│   │   ├── Model3.swift
│   │   └── ModelN.swift
│   ├── Modules
│   │   ├── External Services
│   │   ├── Project
│   │   └── Helpers
│   ├── Networking
│   │   ├── APIConstants.swift
│   │   ├── Services
│   │   │   ├── Service1.swift
│   │   │   ├── Service2.swift
│   │   │   ├── Service3.swift
│   │   │   └── ServiceN.swift
│   │   └── Utils.swift
│   ├── Persistence
│   ├── Resources
│   ├── Info.plist
│   └── User Interface
│       ├── Feature1
│       ├── Feature2
│       ├── Feature3
│       └── FeatureN
├── Project.xcodeproj
├── Project.xcworkspace
├── ProjectTests
├── ProjectUITests
├── Bridging-Header.h
├── Podfile
├── Podfile.lock
├── Pods
├── README.md
├── env.secrets
└── scripts
```

## Minimum iOS version requirement
Unless specified by the client or specific OS-level feature requirements, use the second most-used iOS version. That information can be found at the [Apple App Store Info Page](https://developer.apple.com/support/app-store/).

## Minimum Swift version requirement
Please use Swift 4 or higher.

## Branching model
Use [Git Flow](https://sophilabs.co/blog/git-flow).

## Data Serialization
In case you’re using Swift 4 or higher as recommended before, you can make use of the `Codable` protocol, which gives you seamless JSON/XML/YAML serialization and deserialization without external libraries. For more info take a look at [this Apple-provided documentation](https://developer.apple.com/documentation/foundation/archives_and_serialization/encoding_and_decoding_custom_types). 

In case you’re not using it, please use [SwiftyJSON](https://github.com/SwiftyJSON/SwiftyJSON) (information about using it along _Alamofire_ can be found [here](https://github.com/SwiftyJSON/SwiftyJSON#work-with-alamofire)).

## Code Linting
Use [SwiftLint](https://github.com/realm/SwiftLint).

## Local database
If you want to store data as fast as possible while keeping reliability on that, use [Realm](https://realm.io/). In case you’re experimented with Core Data, we’d suggest you to use it instead.

## Analytics and Crash Reports
For Analytics we use [Fabric](https://fabric.io) and for crash analytics we use [Sentry](https://sentry.com/). Both have excellent guides about how to implement their SDKs into your project’s app.




