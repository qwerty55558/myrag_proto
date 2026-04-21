import com.google.protobuf.gradle.*

plugins {
    java
    `maven-publish`
    id("com.google.protobuf") version "0.9.4"
}

group = "me.clauminirockpt"
version = "1.0.2"

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
    withSourcesJar()
}

repositories {
    mavenCentral()
}

val grpcVersion = "1.72.0"
val protobufVersion = "3.25.5"

dependencies {
    implementation("io.grpc:grpc-protobuf:$grpcVersion")
    implementation("io.grpc:grpc-stub:$grpcVersion")
    implementation("com.google.protobuf:protobuf-java:$protobufVersion")
    compileOnly("org.apache.tomcat:annotations-api:6.0.53")
}

protobuf {
    protoc {
        artifact = "com.google.protobuf:protoc:$protobufVersion"
    }
    plugins {
        create("grpc") {
            artifact = "io.grpc:protoc-gen-grpc-java:$grpcVersion"
        }
    }
    generateProtoTasks {
        all().forEach { task ->
            task.plugins {
                create("grpc")
            }
        }
    }
}

publishing {
    repositories {
        maven {
            name = "GitHubPackages"
            url = uri("https://maven.pkg.github.com/qwerty55558/myrag_proto")
            credentials {
                username = System.getenv("GITHUB_ACTOR") ?: project.findProperty("gpr.user") as String? ?: ""
                password = System.getenv("GITHUB_TOKEN") ?: project.findProperty("gpr.key") as String? ?: ""
            }
        }
    }
    publications {
        create<MavenPublication>("gpr") {
            groupId = "me.clauminirockpt"
            artifactId = "myrag-proto"
            from(components["java"])
        }
    }
}

